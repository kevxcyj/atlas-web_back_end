import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  // Floors setter
  get floors() {
    return this._floors;
  }

  set floors(floorsvalue) {
    if (typeof floorsvalue !== 'number') {
      throw TypeError('Floors must be a number');
    }
    this.floors = floorsvalue;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
