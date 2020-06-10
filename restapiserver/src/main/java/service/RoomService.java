package service;

import dto.Course;
import dto.Seat;
import dto.SelectCourseListByRoomIdResponse;
import mapper.RoomMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RoomService {

  @Autowired
  private RoomMapper mapper;

  public List<SelectCourseListByRoomIdResponse> selectCourseLisByRoomId(int id) {
    return mapper.selectCourseListByRoomId(id);
  }

  public List<Seat> selectSeatListByCourseId(int id) {
    return mapper.selectSeatListByCourseId(id);
  }

  public void updateSeat(Seat seat) {
    mapper.updateSeat(seat);
  }

}
