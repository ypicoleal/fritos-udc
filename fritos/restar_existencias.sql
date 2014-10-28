

create or replace function restar_existencias(venta_id int) returns boolean as 
$BODY$
declare venta venta_ventaproducto%rowtype;
begin
	for venta in (select * from venta_ventaproducto where venta_ventaproducto.venta_id = $1) loop
		update venta_producto set existencia = existencia - venta.cantidad where id = venta.producto_id;
	end loop;
	return true;
end;
$BODY$
language plpgsql;