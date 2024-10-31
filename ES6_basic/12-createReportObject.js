export default function createReportObject(employeesList) {
  const employee = { ...employeesList };

  return {
    employee,
    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };
}
