package controller;

import error.ErrorResponse;
import error.SeatNotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice("controller")
public class ProfessorExceptionAdvice {

  @ExceptionHandler(SeatNotFoundException.class)
  public ResponseEntity<ErrorResponse> seatNotFound() {
    return ResponseEntity
        .status(HttpStatus.NOT_FOUND)
        .body(new ErrorResponse("좌석을 찾을 수 없습니다."));
  }

}
