const { deltaLyftFraudCheck } = require('./deltaLyftFraud');

describe('find users in the loyalty list, not in both other lists', () => {
  test('empty list', () => {
    expect(deltaLyftFraudCheck([],[],[])).toStrictEqual([]);
  });

  test('exact same lists', () => {
    expect(deltaLyftFraudCheck(['u1','u2','u3','u4','u5'],['u1','u2','u3','u4','u5'],['u1','u2','u3','u4','u5'])).toStrictEqual([]);
  });

  test('second list empty', () => {
    expect(deltaLyftFraudCheck(['u1','u2','u3','u4','u5'],[],['u1','u2','u3','u4','u5'])).toStrictEqual(['u1','u2','u3','u4','u5']);
  });

  test('first list empty', () => {
    expect(deltaLyftFraudCheck([],['u1','u2','u3','u4','u5'],['u2','u1','u5','u4','u3'])).toStrictEqual(['u1','u2','u3','u4','u5']);
  });

  test('a user is in integrated list but not in list 1 nor list 2', () => {
    expect(deltaLyftFraudCheck(['u1','u2','u3','u4'],['u1','u2','u3','u4'],['u2','u1','u5','u4','u3'])).toStrictEqual(['u5']);
  });

  test('a few differences in each list', () => {
    expect(deltaLyftFraudCheck(['u1','u2','u3'],['u1','u3','u4'],['u1','u5','u4','u3'])).toStrictEqual(['u4','u5']);
  });

});
