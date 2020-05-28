package service;

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

}
