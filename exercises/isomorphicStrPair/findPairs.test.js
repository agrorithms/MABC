const { countIsoStrPairs } = require('./findPairs');

describe('count isometric pairs', () => {
  test('empty list', () => {
    expect(countIsoStrPairs([])).toBe(0);
  });

  test('multiple pairs', () => {
    expect(countIsoStrPairs(['egg','foo','paper','add','title'])).toBe(4);
  });

  test('no pairs', () => {
    expect(countIsoStrPairs(['foo','bar','hello','world','a','ab'])).toBe(0);
  });

  test('array length = 1', () => {
    expect(countIsoStrPairs(['foo'])).toBe(0);
  });

  test('strings start as pairs but differ in length ', () => {
    expect(countIsoStrPairs(['foo','foobar','two','twofold'])).toBe(0);
  });

  test('same string', () => {
    expect(countIsoStrPairs(['hello','hello','hello','hello'])).toBe(6);
  });

  test('empty strings', () => {
    expect(countIsoStrPairs(['',''])).toBe(1);
  });

  test('spaces/punctuation vs none of that', () => {
    expect(countIsoStrPairs(['a a','a,a', 'aa'])).toBe(1);
  });

  test('capitalization comparison', () => {
    expect(countIsoStrPairs(['aB','ac', 'Ab','AA','aa'])).toBe(4);
  });
});
