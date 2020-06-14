import { student } from './index';

function fetchCourses(userId) {
  return student.get(`${userId}/courses`);
}

function fetchAttendances(userId, courseId) {
  return student.get(`${userId}/courses/${courseId}/attendances`);
}

export { fetchCourses, fetchAttendances };
