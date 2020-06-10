package controller;

import dto.LoginRequest;
import dto.LoginResponse;
import error.MemberNotFoundException;
import mapper.LoginMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import service.LoginService;

@RestController
public class LoginController {

  @Autowired
  private LoginService service;

  @PostMapping("/login")
  public LoginResponse login(@RequestBody LoginRequest request) {
    return service.login(request.getOption(), request.getUsername(), request.getPassword());
  }

}
