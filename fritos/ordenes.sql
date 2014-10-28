create or replace function ordenes() returns text as
$BODY$
declare sql text := '';
declare venta venta_venta%rowtype;
declare comma boolean := false;
begin
	sql := '[';

	 for venta in (select id from venta_venta) loop
		if comma then
			sql := sql || ', ';
		end if;
		sql := sql || '{"productos": ' || (select array_to_json(array(select row_to_json(t) from (select venta_producto.nombre producto, sum(venta_ventaproducto.cantidad) cantidad, venta_producto.precio, sum(venta_ventaproducto.cantidad)*venta_producto.precio subtotal
			from venta_venta join venta_ventaproducto on (venta_venta.id = venta_ventaproducto.venta_id and venta_venta.estado is not false and venta_venta.id = venta.id)
			join venta_producto on (venta_producto.id = venta_ventaproducto.producto_id)
			group by venta_venta.id, venta_producto.id
		) as t))) || ', "venta": '|| venta.id || '}';
		comma := true;
	end loop;
	sql := sql || ']';
	return sql;
end;
$BODY$
language plpgsql;

create or replace function mostrar_venta(venta_id int) returns text as
$BODY$
begin
	return '{"productos": ' || (select array_to_json(array(select row_to_json(t) from (select venta_venta.id venta, venta_producto.nombre producto, sum(venta_ventaproducto.cantidad) cantidad, venta_producto.precio, sum(venta_ventaproducto.cantidad)*venta_producto.precio subtotal
		from venta_venta join venta_ventaproducto on (venta_venta.id = venta_ventaproducto.venta_id and venta_venta.estado is not false and venta_venta.id = $1)
		join venta_producto on (venta_producto.id = venta_ventaproducto.producto_id)
		group by venta_venta.id, venta_producto.id
	) as t))) || ', "venta": '|| $1|| ', "total": '|| (
	select sum(venta_ventaproducto.cantidad*venta_producto.precio)
		from venta_venta join venta_ventaproducto on (venta_venta.id = venta_ventaproducto.venta_id and venta_venta.estado is not false and venta_venta.id = $1)
		join venta_producto on (venta_producto.id = venta_ventaproducto.producto_id)
	) || '}'
	;
end;
$BODY$
language plpgsql;


create or replace function mostrar_dia() returns text as
$BODY$
begin
	return '{"productos": ' || (select array_to_json(array(select row_to_json(t) from (select venta_venta.id venta, venta_producto.nombre producto, sum(venta_ventaproducto.cantidad) cantidad, venta_producto.precio, sum(venta_ventaproducto.cantidad)*venta_producto.precio subtotal
		from venta_venta join venta_ventaproducto on (venta_venta.id = venta_ventaproducto.venta_id and venta_venta.estado = true and venta_venta.fecha::date = current_date)
		join venta_producto on (venta_producto.id = venta_ventaproducto.producto_id)
		group by venta_venta.id, venta_producto.id
	) as t))) || ', "total": '|| (
	select sum(venta_ventaproducto.cantidad*venta_producto.precio)
		from venta_venta join venta_ventaproducto on (venta_venta.id = venta_ventaproducto.venta_id and venta_venta.estado = true and venta_venta.fecha::date = current_date)
		join venta_producto on (venta_producto.id = venta_ventaproducto.producto_id)
	) || '}'
	;
end;
$BODY$
language plpgsql;
