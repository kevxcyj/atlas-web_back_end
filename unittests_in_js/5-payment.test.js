const sinon = require('sinon');
const { sendPaymentRequestToApi } = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('should log the correct total for amounts 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);
    
    sinon.assert.calledWith(consoleSpy, 'The total is: 120');
    sinon.assert.calledOnce(consoleSpy);
  });

  it('should log the correct total for amounts 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);
    
    sinon.assert.calledWith(consoleSpy, 'The total is: 20');
    sinon.assert.calledOnce(consoleSpy);
  });
});