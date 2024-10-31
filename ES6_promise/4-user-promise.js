export default function signupUser(firstName, lastName) {
    const promise = new Promise((resolve) => {
      resolve(
        { firstName, lastName },
      );
    });
    return promise;
  }
