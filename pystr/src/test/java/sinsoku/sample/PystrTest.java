package sinsoku.sample;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

import org.junit.Test;

public class PystrTest {
	@Test
	public void インスタンスを新規作成() throws Exception {
		Pystr str = new Pystr();
		assertThat(str.toString(), is(""));
	}

	@Test
	public void インスタンスを初期化して作成() throws Exception {
		// 文字列で初期化
		Pystr str = new Pystr("abc");
		assertThat(str.toString(), is("abc"));

		// 整数で初期化
		Pystr intstr = new Pystr(0);
		assertThat(intstr.toString(), is("0"));

		// longで初期化
		Pystr lstr = new Pystr(10000000000L);
		assertThat(lstr.toString(), is("10000000000"));

		// 実数で初期化
		Pystr doublestr = new Pystr(0.0);
		assertThat(doublestr.toString(), is("0.0"));

		// 文字で初期化
		Pystr charstr = new Pystr('a');
		assertThat(charstr.toString(), is("a"));

		// 文字配列で初期化
		char[] charr = {'a', 'a', 'a'};
		Pystr carrstr = new Pystr(charr);
		assertThat(carrstr.toString(), is("aaa"));
	}
}
