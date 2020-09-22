package mapper;

import dto.GetStudentFingerprint;
import dto.SimpleStudent;
import dto.Student;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface StudentMapper {

  @Select("select s.id, s.studentCode, s.name from take t, student s " +
      "where t.courseId = #{id} and t.studentId = s.id")
  List<SimpleStudent> selectListByCourseId(@Param("id") int id);

  @Insert("update student set fingerprint = #{finger} where id = #{studentId}")
  void updateFingerprintByStudentId(@Param("finger") String finger, @Param("studentId") int studentId);

  @Select("select id, name, fingerprint from student")
  List<GetStudentFingerprint> selectListForFingerprint();

}
