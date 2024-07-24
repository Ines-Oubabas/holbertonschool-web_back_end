export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }

  let result = '';
  for (const value of set) {
    if (value.startsWith(startString)) {
      if (result.length > 0) {
        result += '-';
      }
      result += value.slice(startString.length);
    }
  }
  return result;
}
