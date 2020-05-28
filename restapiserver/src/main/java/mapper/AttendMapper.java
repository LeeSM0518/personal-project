package mapper;

import dto.Attend;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import java.util.List;

public interface AttendMapper {

  @Select("select id, week, attendance from attend " +
      "where studentId = #{studentId} and courseId = #{courseId}")
  List<Attend> selectListByStudentIdAndCourseId(@Param("studentId") int studentId,
                                                @Param("courseId") int courseId);

  @Insert("insert into attend (studentId, courseId, week, attendance) values " +
      "(#{studentId}, #{courseId}, #{week}, #{attendance})")
  void insertAttend(@Param("studentId") int studentId,
                    @Param("courseId") int courseId,
                    @Param("week") int week,
                    @Param("attendance") String attendance);

  @Update("update attend set attendance=#{attendance} where id=#{attendanceId}")
  void putAttend(@Param("attendance") String attendance,
                 @Param("attendanceId") int id);
  // TODO 컨트롤러, 서비스 구현

}
