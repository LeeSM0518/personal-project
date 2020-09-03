package mapper;

import dto.Seat;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import java.util.List;

public interface SeatMapper {

  @Select("select s.id, seatNumber, name " +
      "from seat s " +
      "         left join student t on s.reserved = t.id " +
      "where roomId = ( " +
      "    select roomid " +
      "    from course " +
      "    where id = #{id} " +
      ") " +
      "order by id;")
  List<Seat> selectListByCourseId(@Param("id") int id);

  @Update("update seat " +
      "set reserved = null " +
      "where roomId = ( " +
      "    select roomId " +
      "    from course " +
      "    where id = 1 " +
      ")")
  void updateByCourseId(@Param("id") int id);

}
