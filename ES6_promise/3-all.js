import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promise = [createUser(), uploadPhoto()];

  return Promise.all(promise)
    .then((results) => {
      const [user, photo] = results;
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
