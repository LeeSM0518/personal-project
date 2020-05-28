package controller;

import error.ErrorResponse;
import error.MemberNotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice("controller")
public class LoginExceptionAdvice {

  @ExceptionHandler(MemberNotFoundException.class)
  public ResponseEntity<ErrorResponse> memberNotFound() {
    return ResponseEntity
        .status(HttpStatus.NOT_FOUND)
        .body(new ErrorResponse("회원을 찾을 수 없습니다."));
  }

}
