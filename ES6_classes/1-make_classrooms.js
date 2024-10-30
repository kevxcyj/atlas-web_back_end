import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const sizes = [19, 20, 34];
  const rooms = sizes.map((sizes) => new ClassRoom(sizes));

  return rooms;
}
