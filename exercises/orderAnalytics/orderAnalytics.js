
function orderAnalysis(orderInput) {
    let output = []
    let customers = {}
    let skus = {}
    ninetyDaysAgo = new Date();
    ninetyDaysAgo.setDate(ninetyDaysAgo.getDate() - 90);
    
    for (order of orderInput) {
        if (!order['returned'] && new Date(order['createdAt'])>=ninetyDaysAgo) {
            console.log(order['id'])
            for (item of order['items']) {
                if (item['category']== 'Books' || item['category']== 'Electronics') {
                    if (!customers[order['customerId']]){
                        customers[order['customerId']] = { customerId: order['customerId'], netSpend: 0, avgUnitPrice: 1, distinctSkus: 0 }
                        skus[order['customerId']]= new Set()
                    }
                    itemPrice=item['price']*item['qty']
                    if (item['coupon']){
                        //console.log('coupon found')
                        if (item['coupon']['type']=='flat') {
                            itemPrice -= item['coupon']['value']
                            //console.log('flat',itemPrice)
                        } else if (item['coupon']['type']=='percent'){
                            itemPrice*=(1-item['coupon']['value']/100)
                            //console.log('percent',itemPrice)
                        } 
                    }
                    skus[order['customerId']].add(item['sku'])
                    thisCustomerMap=customers[order['customerId']]
                    thisCustomerMap['distinctSkus']=skus[order['customerId']].size
                    thisCustomerMap['avgUnitPrice']=(thisCustomerMap['netSpend']+itemPrice)/((thisCustomerMap['netSpend']/thisCustomerMap['avgUnitPrice'])+item['qty'])
                    thisCustomerMap['netSpend']+=itemPrice
                    //console.log(thisCustomerMap)
                    
                }
            
            }
        
        }

    }

    output = Object.values(customers).sort((a, b) => {
        if (a.netSpend > b.netSpend) {
            return -1;
        }
        if (a.netSpend < b.netSpend) {
            return 1;
        } 
        if (a.avgUnitPrice > b.avgUnitPrice){
            return -1;
        }
        if (a.avgUnitPrice < b.avgUnitPrice){
            return 1;
        }
        if (a.customerId < b.customerId){
            return -1;
        }
        if (a.customerId > b.customerId){
            return 1;
        }
    })

    return output.slice(0,3)
}


module.exports = { orderAnalysis };