package controller;

import error.AttendNotFoundException;
import error.CourseNotFoundException;
import error.ErrorResponse;
import error.StudentNotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice("controller")
public class StudentExceptionAdvice {

  @ExceptionHandler(CourseNotFoundException.class)
  public ResponseEntity<ErrorResponse> courseNotFound() {
    return ResponseEntity
        .status(HttpStatus.NOT_FOUND)
        .body(new ErrorResponse("강좌를 찾을 수 없습니다."));
  }

  @ExceptionHandler(AttendNotFoundException.class)
  public ResponseEntity<ErrorResponse> attendNotFound() {
    return ResponseEntity
        .status(HttpStatus.NOT_FOUND)
        .body(new ErrorResponse("출석을 찾을 수 없습니다."));
  }

  @ExceptionHandler(StudentNotFoundException.class)
  public ResponseEntity<ErrorResponse> studentNotFound() {
    return ResponseEntity
        .status(HttpStatus.NOT_FOUND)
        .body(new ErrorResponse("학생을 찾을 수 없습니다."));
  }

}
