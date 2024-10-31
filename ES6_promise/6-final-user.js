import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  return Promise.all([signUpPromise, uploadPromise])
    .then(([signupResult, uploadResult]) => {
      return [
        { status: signupResult.status, value: signupResult.value },
        { status: uploadResult.status, value: uploadResult.value }
      ];
    })
    .catch(error => {
      console.error('Error during profile signup:', error);
      throw error;
    });
}
