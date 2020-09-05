package mapper;

import dto.GetSeatByDevice;
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
      "    where id = #{id} " +
      ")")
  void updateReservedToNullByCourseId(@Param("id") int id);

  @Update("update seat " +
      "set reserved = #{studentId} " +
      "where roomId = #{roomId} and seatNumber = #{seatNumber}")
  void updateReservedToStudentIdByCourseId(@Param("studentId") int studentId,
                                           @Param("roomId") int roomId,
                                           @Param("seatNumber") int seatNumber);

  @Select("select id, seatNumber, reserved from seat where roomid = #{roomId} order by seatNumber")
  List<GetSeatByDevice> selectListByRoomId(@Param("roomId") int roomId);

}
