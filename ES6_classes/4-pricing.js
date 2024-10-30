import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  // Amount setter
  get amount() {
    return this._amount;
  }

  set amount(amountvalue) {
    if (typeof amountvalue !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = amountvalue;
  }

  // Currency setter
  get currency() {
    return this._currency;
  }

  set currency(currencyvalue) {
    if (!(currencyvalue instanceof Currency)) {
      throw new TypeError('Currency must be an instance of Currency class');
    }
    this._currency = currencyvalue;
  }


  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Amount and Conversion Rate must be numbers');
    }
    return conversionRate * amount;
  }
}
