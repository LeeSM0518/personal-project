package mapper;

import dto.Course;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface CourseMapper {

  @Select("select c.id, c.title, c.startTime, c.endTime, c._class, c.day, p.name, r.dong, r.ho " +
      "from take t, course c, professor p, room r " +
      "where t.studentId = #{id} and t.courseId = c.id and c.professorId = p.id and c.roomId = r.id")
  List<Course> selectListByStudentId(@Param("id") int id);

  @Select("select c.id, c.title, c.startTime, c.endTime, c._class, c.day, r.dong, r.ho " +
      "from course c, room r " +
      "where c.professorId = #{id} and c.roomId = r.id")
  List<Course> selectListByProfessorId(@Param("id") int id);

}
