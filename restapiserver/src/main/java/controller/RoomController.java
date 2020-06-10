package controller;

import dto.Seat;
import dto.SelectCourseListByRoomIdResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import service.RoomService;

import java.util.List;

@RestController
@RequestMapping("/rooms")
public class RoomController {

  @Autowired
  private RoomService service;

  @GetMapping("/{roomId}/courses")
  public List<SelectCourseListByRoomIdResponse> getCourseListByRoomId(@PathVariable("roomId") int roomId) {
    return service.selectCourseLisByRoomId(roomId);
  }

  @GetMapping("/{roomId}/courses/{courseId}/seats")
  public List<Seat> getSeatListByCourseId(@PathVariable("courseId") int courseId) {
    return service.selectSeatListByCourseId(courseId);
  }

  @PutMapping("/{roomId}/courses/{courseId}/seats/{seatId}")
  public void putSeat(@RequestBody Seat seat, @PathVariable("seatId") int id) {
    seat.setId(id);
    service.updateSeat(seat);
  }

}
