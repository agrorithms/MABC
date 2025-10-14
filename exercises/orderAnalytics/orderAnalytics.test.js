const { orderAnalysis } = require('./orderAnalytics');


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
    createdAt: "2025-07-10T12:00:00Z",
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

describe('order analyis', () => {
    test('easy sample input', () => {
    expect(orderAnalysis(orders1)).toStrictEqual([
  { customerId: "alice", netSpend: 194.00, avgUnitPrice: 38.80, distinctSkus: 4 },
  { customerId: "yuki",  netSpend: 170.00, avgUnitPrice: 170.00, distinctSkus: 1 },
  { customerId: "bob",   netSpend: 115.00, avgUnitPrice: 28.75, distinctSkus: 2 }
]);
  });
}

)

//AI Tests below

describe('order analysis edge cases', () => {
  test('ignores returned and old orders', () => {
    const orders = [
      {
        id: "o1",
        customerId: "alice",
        createdAt: "2025-08-01T10:00:00Z",
        returned: true,
        items: [{ sku: "B-001", category: "Books", price: 10, qty: 1 }]
      },
      {
        id: "o2",
        customerId: "bob",
        createdAt: "2025-05-01T10:00:00Z", // outside 90 days
        returned: false,
        items: [{ sku: "E-001", category: "Electronics", price: 100, qty: 1 }]
      }
    ];
    expect(orderAnalysis(orders)).toStrictEqual([]); // nothing valid
  });

  test('flat coupon never below zero', () => {
    const orders = [
      {
        id: "o1",
        customerId: "alice",
        createdAt: "2025-08-10T10:00:00Z",
        returned: false,
        items: [
          { sku: "B-001", category: "Books", price: 5, qty: 1, coupon: { type: "flat", value: 10 } }
        ]
      }
    ];
    expect(orderAnalysis(orders)).toStrictEqual([
      { customerId: "alice", netSpend: 0, avgUnitPrice: 0, distinctSkus: 1 }
    ]);
  });

  test('percent coupon applies per line', () => {
    const orders = [
      {
        id: "o1",
        customerId: "bob",
        createdAt: "2025-08-20T10:00:00Z",
        returned: false,
        items: [
          { sku: "E-001", category: "Electronics", price: 100, qty: 1, coupon: { type: "percent", value: 50 } }
        ]
      }
    ];
    expect(orderAnalysis(orders)).toStrictEqual([
      { customerId: "bob", netSpend: 50, avgUnitPrice: 50, distinctSkus: 1 }
    ]);
  });

  test('non-target categories ignored', () => {
    const orders = [
      {
        id: "o1",
        customerId: "zoe",
        createdAt: "2025-09-01T10:00:00Z",
        returned: false,
        items: [{ sku: "T-001", category: "Toys", price: 100, qty: 2 }]
      }
    ];
    expect(orderAnalysis(orders)).toStrictEqual([]); // no Books/Electronics
  });

  test('tie-break by avgUnitPrice then lexicographic customerId', () => {
    const orders = [
      {
        id: "o1",
        customerId: "alice",
        createdAt: "2025-09-01T10:00:00Z",
        returned: false,
        items: [{ sku: "B-001", category: "Books", price: 100, qty: 1 }]
      },
      {
        id: "o2",
        customerId: "bob",
        createdAt: "2025-09-01T10:00:00Z",
        returned: false,
        items: [{ sku: "B-002", category: "Books", price: 50, qty: 2 }]
      },
      {
        id: "o3",
        customerId: "carl",
        createdAt: "2025-09-01T10:00:00Z",
        returned: false,
        items: [{ sku: "B-003", category: "Books", price: 100, qty: 1 }]
      }
    ];
    // alice and carl have same netSpend=100, avgUnitPrice=100
    // break by customerId (alice < carl)
    expect(orderAnalysis(orders)).toStrictEqual([
      { customerId: "alice", netSpend: 100, avgUnitPrice: 100, distinctSkus: 1 },
      { customerId: "carl", netSpend: 100, avgUnitPrice: 100, distinctSkus: 1 },
      { customerId: "bob",  netSpend: 100, avgUnitPrice: 50,  distinctSkus: 1 }
    ]);
  });

  test('fewer than 3 valid customers', () => {
    const orders = [
      {
        id: "o1",
        customerId: "alice",
        createdAt: "2025-09-01T10:00:00Z",
        returned: false,
        items: [{ sku: "B-001", category: "Books", price: 20, qty: 1 }]
      }
    ];
    expect(orderAnalysis(orders)).toStrictEqual([
      { customerId: "alice", netSpend: 20, avgUnitPrice: 20, distinctSkus: 1 }
    ]);
  });
});



//More deterministic AI test for exact checking, however not random

describe("order analysis deterministic large test", () => {
  test("handles large fixed dataset with predictable result", () => {
    const orders = [];

    // alice: 50 Electronics @ $20 each → $1000
    for (let i = 0; i < 50; i++) {
      orders.push({
        id: "a" + i,
        customerId: "alice",
        createdAt: "2025-08-15T10:00:00Z",
        returned: false,
        items: [{ sku: "E-" + i, category: "Electronics", price: 20, qty: 1 }]
      });
    }

    // bob: 25 Books @ $30 each with $10 flat coupon per line → $500 net
    for (let i = 0; i < 25; i++) {
      orders.push({
        id: "b" + i,
        customerId: "bob",
        createdAt: "2025-08-16T10:00:00Z",
        returned: false,
        items: [{
          sku: "B-" + i,
          category: "Books",
          price: 30,
          qty: 1,
          coupon: { type: "flat", value: 10 }
        }]
      });
    }

    // carl: 10 Electronics @ $100 each, 50% off coupon → $500 net
    for (let i = 0; i < 10; i++) {
      orders.push({
        id: "c" + i,
        customerId: "carl",
        createdAt: "2025-08-17T10:00:00Z",
        returned: false,
        items: [{
          sku: "E-C" + i,
          category: "Electronics",
          price: 100,
          qty: 1,
          coupon: { type: "percent", value: 50 }
        }]
      });
    }

    // zoe: mix with Toys (ignored) → only one Books line counts: $40
    for (let i = 0; i < 10; i++) {
      orders.push({
        id: "z" + i,
        customerId: "zoe",
        createdAt: "2025-08-18T10:00:00Z",
        returned: false,
        items: [
          { sku: "T-" + i, category: "Toys", price: 100, qty: 1 },
          { sku: "B-Z" + i, category: "Books", price: 40, qty: 1 }
        ]
      });
    }

    const result = orderAnalysis(orders);

    // Compute expected manually:
    // alice: net 1000, avgUnitPrice=20, distinctSkus=50
    // bob:   net 500, avgUnitPrice=20, distinctSkus=25
    // carl:  net 500, avgUnitPrice=50, distinctSkus=10
    // zoe:   net 400 (10*40), avgUnitPrice=40, distinctSkus=10
    // Top 3 → alice, carl (tie vs bob resolved by avgUnitPrice), bob

    expect(result).toStrictEqual([
      { customerId: "alice", netSpend: 1000, avgUnitPrice: 20, distinctSkus: 50 },
      { customerId: "carl",  netSpend: 500,  avgUnitPrice: 50, distinctSkus: 10 },
      { customerId: "bob",   netSpend: 500,  avgUnitPrice: 20, distinctSkus: 25 }
    ]);
  });
});