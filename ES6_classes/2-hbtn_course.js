export default class HolbertonCourse {
  constructor(name, length, students) {
    this.__name = name;
    this.__length = length;
    this._students = students;
  }


  // Name setter
  get name() {
    return this.name;
  }

  set name(namevalue) {
    if (typeof namevalue !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = namevalue;
  }

  // Length setter
  get length() {
    return this._length;
  }

  set length(lengthvalue) {
    if (typeof lengthvalue !== 'number') {
        throw new TypeError('Length must be a number');
    }
    this._length = lengthvalue;
  }

  // Student setter
  get students() {
    return this._students;
}

  set students(studentvalue) {
    if (!Array.isArray(studentvalue) || !studentvalue.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = newStudents;
  }
}
