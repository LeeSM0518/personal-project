package service;

import dto.GetStudentFingerprint;
import dto.SimpleStudent;
import error.StudentNotFoundException;
import mapper.StudentMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class StudentService {

  @Autowired
  private StudentMapper mapper;

  public List<SimpleStudent> selectListByCourseId(int id) {
    List<SimpleStudent> list = mapper.selectListByCourseId(id);
    if (list == null || list.size() == 0)
      throw new StudentNotFoundException();
    return list;
  }

  public void updateFingerprintByStudentId(String finger, int studentId) {
    mapper.updateFingerprintByStudentId(finger, studentId);
  }

  public List<GetStudentFingerprint> selectListForFingerprint() {
    return mapper.selectListForFingerprint();
  }

}
