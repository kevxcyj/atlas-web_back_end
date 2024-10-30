export default function getListStudentsIds(studentList) {
  return Array.isArray(studentList) ? studentList.map(student => student.id) : [];
}
