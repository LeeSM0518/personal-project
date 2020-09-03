import { professor, student } from './index';

function fetchCourse(professorId) {
  return professor.get(`${professorId}/courses`);
}

function fetchStudentsInCourses(professorId, courseId) {
  return professor.get(`${professorId}/courses/${courseId}/students`);
}

function fetchAttendanceByStudent(professorId, courseId, studentId) {
  return professor.get(
    `${professorId}/courses/${courseId}/students/${studentId}/attendances`,
  );
}

function putAttendance(professorId, courseId, studentId, attend) {
  return professor.put(
    `${professorId}/courses/${courseId}/students/${studentId}/attendances/${attend.id}`,
    attend,
  );
}

function fetchSeats(professorId, courseId) {
  return professor.get(`${professorId}/courses/${courseId}/seats`);
}

function updateAllSeat(professorId, courseId) {
  return professor.put(`${professorId}/courses/${courseId}/seats`);
}

export {
  fetchCourse,
  updateAllSeat,
  fetchStudentsInCourses,
  fetchAttendanceByStudent,
  putAttendance,
  fetchSeats,
};
