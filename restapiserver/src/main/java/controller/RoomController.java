package controller;

import dto.RoomDto;
import dto.Seat;
import dto.SelectCourseListByRoomIdResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import service.CourseService;
import service.RoomService;

import java.util.List;

@RestController
@RequestMapping("/rooms")
public class RoomController {

  @Autowired
  private RoomService roomService;

  @GetMapping("/{roomId}/courses")
  public List<SelectCourseListByRoomIdResponse> getCourseListByRoomId(@PathVariable("roomId") int roomId) {
    return roomService.selectCourseLisByRoomId(roomId);
  }

  @GetMapping("/{roomId}/courses/{courseId}/seats")
  public List<Seat> getSeatListByCourseId(@PathVariable("courseId") int courseId) {
    return roomService.selectSeatListByCourseId(courseId);
  }

  @PutMapping("/{roomId}/courses/{courseId}/seats/{seatId}")
  public void putSeat(@RequestBody Seat seat, @PathVariable("seatId") int id) {
    seat.setId(id);
    roomService.updateSeat(seat);
  }

  @GetMapping
  public List<RoomDto> getAll() {
    return roomService.selectAll();
  }

}
