package mapper;

import dto.Professor;
import dto.Student;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

public interface LoginMapper {

  @Select("select id, name from professor where professorCode=#{code} and password=#{password}")
  Professor selectOneProfessorByCodeAndPassWord(@Param("code") String code, @Param("password") String password);

  @Select("select id, name from student where studentCode=#{code} and password=#{password}")
  Student selectOneStudentByCodeAndPassWord(@Param("code") String code, @Param("password") String password);

}
