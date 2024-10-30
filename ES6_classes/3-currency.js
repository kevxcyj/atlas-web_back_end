export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // Code setter
  get code() {
    return this._code;
  }

  set code(codevalue) {
    if (typeof codevalue !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = codevalue;
  }

  // Name setter
  get name() {
    return this._name;
  }

  set name(namevalue) {
    if (typeof namevalue !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = namevalue;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
