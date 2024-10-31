export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(newSize) {
    if (typeof newSize !== 'number' || newSize <= 0) {
      throw new Error('Size must be a non-zero number'); this._size = newSize;
    }
  }
  
  get location() {
    return this._location;
  }
  
  set location(newLocation) {
    if (typeof newLocation !== 'string' || newLocation.length <= 0) {
      throw new Error('Location must be a non-empty string'); this._location = newLocation;
    }
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
