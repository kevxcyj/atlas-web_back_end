import getListStudents from "./0-get_list_students.js";

export default function getStudentsByLocation(location) {
  const students = getListStudents();

  return students.filter(student => student.location === location);
}
