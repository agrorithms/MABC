type Order = {
    id: string
    returned: boolean
    createdAt: string
    items: Array<Item>
    customerId: string
}

type Item = {
    category: string
    price: number
    qty: number
    coupon?: {
        type: 'flat' | 'percent'
        value: number
    }
    /**stock keeping unit */
    sku: string
}


type ItemSummary = {
    netSpend: number
    totalQty: number
    /**distinct stock keeping units */
    distinctSkus: Set<string>

}

type CustomerInfo = {
    netSpend: number
    avgUnitPrice: number
    customerId: string
    distinctSkus: number
}

interface CustomerSummary {
    [customerId: string]: CustomerInfo
}

interface CustomerSkus {
    [customerId: string]: Set<string>
}

interface Accumulator {
    customerSummary: CustomerSummary;
    customerSkus: CustomerSkus;
}


function calculatePrice(item: Item) {
    let lineItemPrice = item.price * item.qty
    if (item['coupon']) {
        if (item['coupon']['type'] == 'flat') {
            lineItemPrice -= item['coupon']['value']
            if (lineItemPrice < 0) {
                lineItemPrice = 0
            }
        } else {
            lineItemPrice *= (1 - item['coupon']['value'] / 100)
        }
    }
    return lineItemPrice

}

function initializeCustomer(newCustomer: string, existingCustomers: Accumulator, itemSummary: ItemSummary) {
    existingCustomers.customerSkus[newCustomer] = itemSummary.distinctSkus;
    existingCustomers.customerSummary[newCustomer] = {
        'customerId': newCustomer,
        'netSpend': itemSummary.netSpend,
        'avgUnitPrice': itemSummary.netSpend / itemSummary.totalQty,
        'distinctSkus': itemSummary.distinctSkus.size
    };
    return existingCustomers
}

function updateCustomer(customer: string, existingCustomers: Accumulator, itemSummary: ItemSummary) {
    let newTotalQty = (existingCustomers.customerSummary[customer].netSpend / existingCustomers.customerSummary[customer].avgUnitPrice) + itemSummary.totalQty;
    let newNetSpend = existingCustomers.customerSummary[customer].netSpend + itemSummary.netSpend;
    existingCustomers.customerSummary[customer].avgUnitPrice = newNetSpend / newTotalQty;
    existingCustomers.customerSummary[customer].netSpend += itemSummary.netSpend;
    existingCustomers.customerSkus[customer] = new Set([...existingCustomers.customerSkus[customer], ...itemSummary.distinctSkus]);
    existingCustomers.customerSummary[customer].distinctSkus = existingCustomers.customerSkus[customer].size;
    return existingCustomers
}

function orderAnalysis(orderInput: Array<Order>) {
    const ninetyDaysAgo = new Date();
    ninetyDaysAgo.setDate(ninetyDaysAgo.getDate() - 90);
    const accInitial: Accumulator = { customerSummary: {}, customerSkus: {} };
    const customersInfo = orderInput.filter((order, i) => !order.returned && new Date(order.createdAt) >= ninetyDaysAgo)
        .reduce((acc, order) => {
            const innerAccInitial: ItemSummary = { netSpend: 0, totalQty: 0, distinctSkus: new Set() };
            const filtereditems = order.items.filter((item) => item.category == 'Books' || item.category == 'Electronics');
            const itemSummary = filtereditems.reduce((innerAcc, item) => {
                innerAcc.netSpend += calculatePrice(item)
                innerAcc.totalQty += item.qty
                innerAcc.distinctSkus.add(item.sku)
                return innerAcc
            }, innerAccInitial);

            if (itemSummary.totalQty !== 0) {

                if (!(acc.customerSummary[order.customerId])) {
                    acc = initializeCustomer(order.customerId, acc, itemSummary)
                } else {
                    acc = updateCustomer(order.customerId, acc, itemSummary)
                }
                //acc.customerSummary[order.customerId].distinctSkus = acc.customerSkus[order.customerId].size
            }
            return acc;
        }, accInitial)
    return Object.values(customersInfo.customerSummary).sort((a: CustomerInfo, b: CustomerInfo) => {
        const spendDiff: number = b.netSpend - a.netSpend;
        const aupDiff: number = b.avgUnitPrice - a.avgUnitPrice;
        if (spendDiff !== 0) return spendDiff;
        else if (aupDiff !== 0) return aupDiff;
        else return a.customerId.localeCompare(b.customerId);
    }).slice(0, 3)
};


module.exports = { orderAnalysis };