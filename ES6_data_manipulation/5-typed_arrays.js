export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const bufferview = new DataView(buffer, 0, length);

  if (position < 0 || position >= length) {
    throw Error('Position outside range');
  }
  bufferview.setInt8(position, value);
  return bufferview;
}
