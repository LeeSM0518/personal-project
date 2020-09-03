package mapper;

import dto.Attend;
import dto.AttendForProfessor;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import java.util.List;

public interface AttendMapper {

  @Select("select id, week, attendance from attend " +
      "where studentId = #{studentId} and courseId = #{courseId} order by week")
  List<Attend> selectListByStudentIdAndCourseId(@Param("studentId") int studentId,
                                                @Param("courseId") int courseId);

  @Select("select s.id, s.studentCode, s.name, count(s.name), sum(a.attendance) " +
      "from take t, " +
      "     student s, " +
      "     attend a " +
      "where t.courseId = #{courseId} " +
      "  and t.studentId = s.id " +
      "  and a.studentid = s.id " +
      "  and t.courseid = a.courseid " +
      "group by s.id, s.studentcode, s.name " +
      "order by studentcode")
  List<AttendForProfessor> selectStudentAndAttendByStudentIdAndCourseId(@Param("courseId") int courseId);

  @Insert("insert into attend (studentId, courseId, week, attendance) values " +
      "(#{studentId}, #{courseId}, #{week}, #{attendance})")
  void insertAttend(@Param("studentId") int studentId,
                    @Param("courseId") int courseId,
                    @Param("week") int week,
                    @Param("attendance") double attendance);

  @Update("update attend set attendance=#{attendance} where id=#{id}")
  void putAttend(Attend attend);

}
