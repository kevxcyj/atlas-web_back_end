export default function cleanSet(set, startString) {
  if (startString && typeof startString === 'string') {
    const newarray = [];
    for (const item of set) {
      if (item.startsWith(startString)) {
        newarray.push(item.slice(startString.length));
      }
    }
    return newarray.join('-');
  }
  return '';
}
