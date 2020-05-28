package service;

import dto.Attend;
import dto.AttendPostRequest;
import error.AttendNotFoundException;
import mapper.AttendMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AttendService {

  @Autowired
  private AttendMapper mapper;

  public List<Attend> selectListByStudentIdAndCourseId(int studentId, int courseId) {
    List<Attend> list = mapper.selectListByStudentIdAndCourseId(studentId, courseId);
    if (list == null || list.size() == 0)
      throw new AttendNotFoundException();
    return list;
  }

  public void insertAttend(int studentId, int courseId, AttendPostRequest request) {
    mapper.insertAttend(studentId, courseId, request.getWeek(), request.getAttendance());
  }

}
