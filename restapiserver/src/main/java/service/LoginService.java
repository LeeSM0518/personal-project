package service;

import dto.LoginResponse;
import dto.Professor;
import dto.Student;
import error.MemberNotFoundException;
import mapper.LoginMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LoginService {

  @Autowired
  private LoginMapper mapper;

  public LoginResponse login(String option, String code, String password) {
    return option.equals("professor") ?
        loginForProfessor(code, password) : loginForStudent(code, password);
  }

  public LoginResponse loginByDevice(String option, String code, String birthday) {
    return option.equals("professor") ?
        loginForProfessorByDevice(code, birthday) : loginForStudentByDevice(code, birthday);
  }


  private LoginResponse loginForProfessor(String code, String password) {
    Professor professor = mapper.selectOneProfessorByCodeAndPassWord(code, password);
    if (professor == null || professor.getName().equals(""))
      throw new MemberNotFoundException();
    return new LoginResponse(professor.getId(), professor.getName());
  }

  private LoginResponse loginForStudent(String code, String password) {
    Student student = mapper.selectOneStudentByCodeAndPassWord(code, password);
    if (student == null || student.getName().equals(""))
      throw new MemberNotFoundException();
    return new LoginResponse(student.getId(), student.getName());
  }

  private LoginResponse loginForProfessorByDevice(String code, String birthday) {
    Professor professor = mapper.selectOneProfessorByCodeAndBirthday(code, birthday);
    if (professor == null || professor.getName().equals(""))
      throw new MemberNotFoundException();
    return new LoginResponse(professor.getId(), professor.getName());
  }

  private LoginResponse loginForStudentByDevice(String code, String birthday) {
    Student student = mapper.selectOneStudentByCodeAndBirthday(code, birthday);
    if (student == null || student.getName().equals(""))
      throw new MemberNotFoundException();
    return new LoginResponse(student.getId(), student.getName());
  }

}
