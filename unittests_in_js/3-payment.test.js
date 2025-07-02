const sinon = require('sinon');
const { sendPaymentRequestToApi } = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with correct arguments', () => {
    const spy = sinon.spy(require('./utils'), 'calculateNumber');
    
    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledWith(spy, 'SUM', 100, 20);
    sinon.assert.calledOnce(spy);

    spy.restore();
  });

  it('should log the correct total', () => {
    const spy = sinon.spy(console, 'log');
    
    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledWith(spy, 'The total is: 120');

    spy.restore();
  });
});