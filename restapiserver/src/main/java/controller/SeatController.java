package controller;

import dto.GetSeatByDevice;
import dto.PutOneSeatByDeviceDto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import service.SeatService;

import java.util.List;

@RestController
public class SeatController {

  @Autowired
  private SeatService seatService;

  @PutMapping("/seats")
  public void putSeatByStudentIdAndCourseId(@RequestBody PutOneSeatByDeviceDto dto) {
    seatService.updateReservedToStudentIdByCourseId(dto.getStudentId(), dto.getRoomId(), dto.getSeatNumber());
  }

  @GetMapping("/rooms/{roomId}/seats")
  public List<GetSeatByDevice> getSeatsByRoomId(@PathVariable("roomId") int roomId) {
    return seatService.selectListByRoomId(roomId);
  }

}
