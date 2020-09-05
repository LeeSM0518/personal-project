package service;

import dto.GetSeatByDevice;
import dto.Seat;
import error.SeatNotFoundException;
import mapper.SeatMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SeatService {

  @Autowired
  private SeatMapper mapper;

  public List<Seat> selectListByCourseId(int id) {
    List<Seat> list = mapper.selectListByCourseId(id);
    if (list == null || list.size() == 0)
      throw new SeatNotFoundException();
    return list;
  }

  public void updateByCourseId(int id) {
    mapper.updateReservedToNullByCourseId(id);
  }

  public void updateReservedToStudentIdByCourseId(int studentId, int roomId, int seatNumber) {
    mapper.updateReservedToStudentIdByCourseId(studentId, roomId, seatNumber);
  }

  public List<GetSeatByDevice> selectListByRoomId(int roomId) {
    return mapper.selectListByRoomId(roomId);
  }

}
