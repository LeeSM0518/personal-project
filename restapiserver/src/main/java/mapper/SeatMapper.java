package mapper;

import dto.Seat;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface SeatMapper {

  @Select("select s.id, s.seatNumber, s.status from course c, seat s " +
      "where c.id = #{id} and c.roomId = s.roomId")
  List<Seat> selectListByCourseId(@Param("id") int id);

}
