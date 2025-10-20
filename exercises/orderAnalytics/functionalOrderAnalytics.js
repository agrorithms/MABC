function orderAnalysis(orderInput) {
	let ninetyDaysAgo = new Date();
    ninetyDaysAgo.setDate(ninetyDaysAgo.getDate() - 90);
    return Object.values(Object.values(orderInput.filter((order) => !order.returned && new Date(order.createdAt)>=ninetyDaysAgo)
    									 .reduce((acc, order) => {
                            let filtereditems = order.items.filter((item) => item.category == 'Books' || item.category == 'Electronics')
                            let itemSummary = filtereditems.reduce((innerAcc, item) => {
                                innerAcc.netSpend += item.price*item.qty //coupon calcualtion to be added
                                innerAcc.totalQty += item.qty
                                innerAcc.distinctSkus.add(item.sku)
                                return innerAcc
                            }, {netSpend : 0 , totalQty : 0, distinctSkus : new Set() });
                        
                            if (itemSummary.totalQty!==0){ 
                                if (!(acc.customerSummary[order.customerId])) {
                                    acc.customerSummary[order.customerId] ={}
                                    acc.customerSummary[order.customerId].customerId =order.customerId
                                    acc.customerSummary[order.customerId].netSpend = itemSummary.netSpend
                                    acc.customerSummary[order.customerId].avgUnitPrice = itemSummary.netSpend/itemSummary.totalQty
                                    acc.customerSkus[order.customerId] = itemSummary.distinctSkus
                                    	
                                } else {
                                    //console.log(itemSummary,acc.customerSummary[order.customerId])
                                    
                                    acc.customerSummary[order.customerId].avgUnitPrice= (acc.customerSummary[order.customerId].netSpend+itemSummary.netSpend)/((acc.customerSummary[order.customerId].netSpend/acc.customerSummary[order.customerId].avgUnitPrice)+itemSummary.totalQty)
                                    acc.customerSummary[order.customerId].netSpend+=itemSummary.netSpend
                                    acc.customerSkus[order.customerId]=acc.customerSkus[order.customerId].union(itemSummary.distinctSkus)
                                    
                                }
                                acc.customerSummary[order.customerId].distinctSkus = acc.customerSkus[order.customerId].size
                            }
                            //console.log(acc.customerSummary[order.customerId])
                            return acc;
                        }, {customerSummary : {}, customerSkus : {}}))[0]).sort((a, b) => {
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
                        }).slice(0,3) 
    }; 


const orders1 = [
  {
    id: "o1",
    customerId: "alice",
    createdAt: "2025-08-15T10:00:00Z",
    returned: false,
    items: [
      { sku: "B-001", category: "Books",       price: 12.00, qty: 2 },
      { sku: "E-010", category: "Electronics", price: 50.00, qty: 1,
        coupon: { type: "percent", value: 10 } } // 10% off
    ]
  },
  {
    id: "o2",
    customerId: "bob",
    createdAt: "2025-08-10T12:00:00Z",
    returned: false,
    items: [
      { sku: "E-020", category: "Electronics", price: 80.00, qty: 1 },
      { sku: "B-002", category: "Books",       price: 15.00, qty: 3,
        coupon: { type: "flat", value: 10 } }  // $10 off this line (not each book)
    ]
  },
  {
    id: "o3", // OUT of 90-day window → excluded
    customerId: "alice",
    createdAt: "2025-06-01T09:00:00Z",
    returned: false,
    items: [{ sku: "B-005", category: "Books", price: 20.00, qty: 1 }]
  },
  {
    id: "o4",
    customerId: "zoe", // won't have greater netSpend that yuki
    createdAt: "2025-08-28T16:00:00Z",
    returned: false,
    items: [
      { sku: "E-010", category: "Electronics", price: 55.00, qty: 2,
        coupon: { type: "percent", value: 20 } }, // 20% off
      { sku: "B-003", category: "Books",       price: 25.00, qty: 1 }
    ]
  },
  {
    id: "o5", // returned → excluded
    customerId: "bob",
    createdAt: "2025-08-30T14:00:00Z",
    returned: true,
    items: [{ sku: "B-002", category: "Books", price: 15.00, qty: 1 }]
  },
  {
    id: "o6",
    customerId: "yuki",
    createdAt: "2025-08-01T10:00:00Z",
    returned: false,
    items: [
      { sku: "E-030", category: "Electronics", price: 200.00, qty: 1,
        coupon: { type: "flat", value: 30 } },   // $30 off
      { sku: "T-001", category: "Toys",        price: 30.00,  qty: 2 } // non-target category
    ]
  },
  {
    id: "o7",
    customerId: "alice",
    createdAt: "2025-09-01T11:00:00Z",
    returned: false,
    items: [
      { sku: "B-004", category: "Books",       price: 30.00, qty: 1,
        coupon: { type: "flat", value: 5 } },   // $5 off
      { sku: "E-040", category: "Electronics", price: 100.00, qty: 1 }
    ]
  },
  {
    id: "o8", // OUT of 90-day window → excluded
    customerId: "zoe",
    createdAt: "2025-05-30T10:00:00Z",
    returned: false,
    items: [{ sku: "B-006", category: "Books", price: 10.00, qty: 1 }]
  }
];

console.log(orderAnalysis(orders1))


module.exports = { orderAnalysis };