package controller;

import dto.LoginRequest;
import dto.LoginRequestByDevice;
import dto.LoginResponse;
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

  @PostMapping("/devicelogin")
  public LoginResponse loginByDevice(@RequestBody LoginRequestByDevice request) {
    return service.loginByDevice(request.getOption(), request.getUsername(), request.getBirthday());
  }

}
