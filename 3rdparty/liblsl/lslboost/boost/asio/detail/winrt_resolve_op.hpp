//
// detail/winrt_resolve_op.hpp
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
// Copyright (c) 2003-2018 Christopher M. Kohlhoff (chris at kohlhoff dot com)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
//

#ifndef BOOST_ASIO_DETAIL_WINRT_RESOLVE_OP_HPP
#define BOOST_ASIO_DETAIL_WINRT_RESOLVE_OP_HPP

#if defined(_MSC_VER) && (_MSC_VER >= 1200)
# pragma once
#endif // defined(_MSC_VER) && (_MSC_VER >= 1200)

#include <boost/asio/detail/config.hpp>

#if defined(BOOST_ASIO_WINDOWS_RUNTIME)

#include <boost/asio/detail/bind_handler.hpp>
#include <boost/asio/detail/fenced_block.hpp>
#include <boost/asio/detail/handler_alloc_helpers.hpp>
#include <boost/asio/detail/handler_invoke_helpers.hpp>
#include <boost/asio/detail/memory.hpp>
#include <boost/asio/detail/winrt_async_op.hpp>
#include <boost/asio/ip/basic_resolver_results.hpp>
#include <boost/asio/error.hpp>

#include <boost/asio/detail/push_options.hpp>

namespace lslboost {
namespace asio {
namespace detail {

template <typename Protocol, typename Handler>
class winrt_resolve_op :
  public winrt_async_op<
    Windows::Foundation::Collections::IVectorView<
      Windows::Networking::EndpointPair^>^>
{
public:
  BOOST_ASIO_DEFINE_HANDLER_PTR(winrt_resolve_op);

  typedef typename Protocol::endpoint endpoint_type;
  typedef lslboost::asio::ip::basic_resolver_query<Protocol> query_type;
  typedef lslboost::asio::ip::basic_resolver_results<Protocol> results_type;

  winrt_resolve_op(const query_type& query, Handler& handler)
    : winrt_async_op<
        Windows::Foundation::Collections::IVectorView<
          Windows::Networking::EndpointPair^>^>(
            &winrt_resolve_op::do_complete),
      query_(query),
      handler_(BOOST_ASIO_MOVE_CAST(Handler)(handler))
  {
    handler_work<Handler>::start(handler_);
  }

  static void do_complete(void* owner, operation* base,
      const lslboost::system::error_code&, std::size_t)
  {
    // Take ownership of the operation object.
    winrt_resolve_op* o(static_cast<winrt_resolve_op*>(base));
    ptr p = { lslboost::asio::detail::addressof(o->handler_), o, o };
    handler_work<Handler> w(o->handler_);

    BOOST_ASIO_HANDLER_COMPLETION((*o));

    results_type results = results_type();
    if (!o->ec_)
    {
      try
      {
        results = results_type::create(o->result_, o->query_.hints(),
            o->query_.host_name(), o->query_.service_name());
      }
      catch (Platform::Exception^ e)
      {
        o->ec_ = lslboost::system::error_code(e->HResult,
            lslboost::system::system_category());
      }
    }

    // Make a copy of the handler so that the memory can be deallocated before
    // the upcall is made. Even if we're not about to make an upcall, a
    // sub-object of the handler may be the true owner of the memory associated
    // with the handler. Consequently, a local copy of the handler is required
    // to ensure that any owning sub-object remains valid until after we have
    // deallocated the memory here.
    detail::binder2<Handler, lslboost::system::error_code, results_type>
      handler(o->handler_, o->ec_, results);
    p.h = lslboost::asio::detail::addressof(handler.handler_);
    p.reset();

    // Make the upcall if required.
    if (owner)
    {
      fenced_block b(fenced_block::half);
      BOOST_ASIO_HANDLER_INVOCATION_BEGIN((handler.arg1_, "..."));
      w.complete(handler, handler.handler_);
      BOOST_ASIO_HANDLER_INVOCATION_END;
    }
  }

private:
  query_type query_;
  Handler handler_;
};

} // namespace detail
} // namespace asio
} // namespace lslboost

#include <boost/asio/detail/pop_options.hpp>

#endif // defined(BOOST_ASIO_WINDOWS_RUNTIME)

#endif // BOOST_ASIO_DETAIL_WINRT_RESOLVE_OP_HPP
