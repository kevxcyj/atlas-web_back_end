export default function getStudentsByLocation(location) {
  const students = getListStudents();

  return students.filter(student => student.location === location);
}
