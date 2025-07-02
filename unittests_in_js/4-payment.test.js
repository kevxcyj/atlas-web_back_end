const sinon = require('sinon');
const { sendPaymentRequestToApi } = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  beforeEach(() => {
    sinon.stub(require('./utils'), 'calculateNumber').returns(10);
    
    sinon.spy(console, 'log');
  });

  afterEach(() => {
    require('./utils').calculateNumber.restore();
    console.log.restore();
  });

  it('should call Utils.calculateNumber with correct arguments', () => {
    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledWith(require('./utils').calculateNumber, 'SUM', 100, 20);
    sinon.assert.calledOnce(require('./utils').calculateNumber);
  });

  it('should log the correct total', () => {
    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledWith(console.log, 'The total is: 10');
    sinon.assert.calledOnce(console.log);
  });
});