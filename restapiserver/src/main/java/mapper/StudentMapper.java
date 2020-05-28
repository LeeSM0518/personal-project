package mapper;

import dto.SimpleStudent;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface StudentMapper {

  @Select("select s.id, s.studentCode, s.name from take t, student s " +
      "where t.courseId = #{id} and t.studentId = s.id")
  List<SimpleStudent> selectListByCourseId(@Param("id") int id);

}
