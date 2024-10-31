export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      const value = { status: 200, body: 'Success' };
      resolve(value); 
    } else {
      reject(new TypeError('The fake API is not working currently'));
    }
  });
}
